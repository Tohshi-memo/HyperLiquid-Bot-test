# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T15:37:31.202920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6575` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `0.3843` n `230`; crypto_major avg `0.3689` n `8`; equity avg `0.1135` n `94`; fx avg `-0.0042` n `6`; index avg `0.062` n `25`; metal avg `0.0692` n `20`; unknown avg `0.231` n `768`
- 1h: commodity avg `-0.2118` n `12`; crypto_alt avg `0.1011` n `230`; crypto_major avg `-0.0652` n `8`; equity avg `-0.4747` n `94`; fx avg `-0.0304` n `6`; index avg `-0.0181` n `25`; metal avg `0.078` n `20`; unknown avg `0.0134` n `768`
- 4h: commodity avg `-0.1702` n `12`; crypto_alt avg `0.7661` n `230`; crypto_major avg `0.4761` n `8`; equity avg `-1.1814` n `94`; fx avg `0.0046` n `6`; index avg `0.0027` n `25`; metal avg `-0.1147` n `20`; unknown avg `0.2776` n `768`
- 24h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.6125` n `230`; crypto_major avg `-1.3895` n `8`; equity avg `-2.5963` n `94`; fx avg `-0.0534` n `6`; index avg `-0.2248` n `25`; metal avg `-0.1971` n `20`; unknown avg `-0.2638` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
