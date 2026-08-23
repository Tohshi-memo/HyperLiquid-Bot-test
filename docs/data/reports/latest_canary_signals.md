# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T12:11:35.567915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.1799` n `230`; crypto_major avg `-0.5238` n `8`; equity avg `-0.012` n `121`; fx avg `0.0034` n `6`; index avg `0.0046` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.4053` n `795`
- 1h: commodity avg `0.0013` n `12`; crypto_alt avg `0.5288` n `230`; crypto_major avg `0.2514` n `8`; equity avg `0.075` n `121`; fx avg `0.0027` n `6`; index avg `0.0082` n `25`; metal avg `0.02` n `20`; unknown avg `1.6857` n `795`
- 4h: commodity avg `-0.0351` n `12`; crypto_alt avg `2.0677` n `230`; crypto_major avg `0.9535` n `8`; equity avg `0.2262` n `121`; fx avg `-0.0124` n `6`; index avg `0.0376` n `25`; metal avg `0.0195` n `20`; unknown avg `0.9627` n `794`
- 24h: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.2551` n `230`; crypto_major avg `0.1248` n `8`; equity avg `0.3996` n `121`; fx avg `0.0345` n `6`; index avg `0.0394` n `25`; metal avg `0.0522` n `20`; unknown avg `3.5267` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
