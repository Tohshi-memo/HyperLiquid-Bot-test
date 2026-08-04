# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T22:22:32.284570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `0.0173` n `230`; crypto_major avg `-0.0268` n `8`; equity avg `0.0728` n `108`; fx avg `-0.0008` n `6`; index avg `0.0143` n `25`; metal avg `0.0285` n `20`; unknown avg `-0.0104` n `781`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.0364` n `230`; crypto_major avg `-0.0535` n `8`; equity avg `0.1652` n `108`; fx avg `-0.004` n `6`; index avg `0.0199` n `25`; metal avg `0.0384` n `20`; unknown avg `0.0375` n `781`
- 4h: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.0122` n `230`; crypto_major avg `-0.2522` n `8`; equity avg `-0.4935` n `108`; fx avg `0.0343` n `6`; index avg `-0.0458` n `25`; metal avg `-0.0843` n `20`; unknown avg `0.0251` n `781`
- 24h: commodity avg `-1.2089` n `12`; crypto_alt avg `0.0739` n `230`; crypto_major avg `0.6909` n `8`; equity avg `3.0393` n `107`; fx avg `0.1012` n `6`; index avg `0.706` n `25`; metal avg `0.9265` n `20`; unknown avg `0.4389` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
