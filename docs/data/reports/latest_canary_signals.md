# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T14:52:27.050338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.7078` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1323` n `12`; crypto_alt avg `-0.0122` n `230`; crypto_major avg `-0.1037` n `8`; equity avg `-0.4405` n `94`; fx avg `-0.0263` n `6`; index avg `-0.0543` n `25`; metal avg `-0.0368` n `20`; unknown avg `-0.0349` n `768`
- 1h: commodity avg `-0.2944` n `12`; crypto_alt avg `0.2381` n `230`; crypto_major avg `0.3127` n `8`; equity avg `-0.0956` n `94`; fx avg `-0.0333` n `6`; index avg `0.0641` n `25`; metal avg `0.0104` n `20`; unknown avg `0.1008` n `768`
- 4h: commodity avg `-0.1274` n `12`; crypto_alt avg `0.6005` n `230`; crypto_major avg `0.3731` n `8`; equity avg `-1.3347` n `94`; fx avg `0.0014` n `6`; index avg `-0.0804` n `25`; metal avg `-0.27` n `20`; unknown avg `0.2106` n `768`
- 24h: commodity avg `0.0497` n `12`; crypto_alt avg `-0.7199` n `230`; crypto_major avg `-1.5386` n `8`; equity avg `-2.698` n `94`; fx avg `-0.0707` n `6`; index avg `-0.2237` n `25`; metal avg `-0.4187` n `20`; unknown avg `-0.1777` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
