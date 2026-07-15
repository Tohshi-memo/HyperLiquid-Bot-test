# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T02:52:32.299445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7137` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0279` n `12`; crypto_alt avg `-0.0801` n `230`; crypto_major avg `0.1325` n `8`; equity avg `0.2011` n `93`; fx avg `0.0101` n `6`; index avg `-0.0041` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.1222` n `767`
- 1h: commodity avg `0.0519` n `12`; crypto_alt avg `-0.2826` n `230`; crypto_major avg `0.1274` n `8`; equity avg `0.6467` n `93`; fx avg `0.005` n `6`; index avg `0.0925` n `25`; metal avg `0.0291` n `20`; unknown avg `-0.2523` n `767`
- 4h: commodity avg `0.1112` n `12`; crypto_alt avg `-0.2802` n `230`; crypto_major avg `-0.4403` n `8`; equity avg `1.2734` n `93`; fx avg `0.0449` n `6`; index avg `0.1587` n `25`; metal avg `0.0277` n `20`; unknown avg `-0.4618` n `765`
- 24h: commodity avg `0.22` n `12`; crypto_alt avg `1.7183` n `230`; crypto_major avg `2.871` n `8`; equity avg `2.7345` n `92`; fx avg `0.0851` n `6`; index avg `0.7136` n `25`; metal avg `0.5273` n `20`; unknown avg `0.2057` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
