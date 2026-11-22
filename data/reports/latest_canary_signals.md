# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T13:37:38.346959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `13`; crypto_alt avg `0.0717` n `239`; crypto_major avg `0.109` n `8`; equity avg `0.0615` n `166`; fx avg `0.0041` n `6`; index avg `0.0447` n `27`; metal avg `-0.004` n `20`; unknown avg `0.2649` n `1263`
- 1h: commodity avg `-0.0037` n `13`; crypto_alt avg `0.3105` n `239`; crypto_major avg `0.3884` n `8`; equity avg `0.2861` n `166`; fx avg `0.0098` n `6`; index avg `0.0856` n `27`; metal avg `0.0146` n `20`; unknown avg `1.0108` n `1261`
- 4h: commodity avg `-0.0006` n `13`; crypto_alt avg `0.886` n `239`; crypto_major avg `0.8096` n `8`; equity avg `0.5709` n `166`; fx avg `0.0019` n `6`; index avg `0.098` n `27`; metal avg `0.0416` n `20`; unknown avg `130.9717` n `1149`
- 24h: commodity avg `-0.0009` n `13`; crypto_alt avg `0.8623` n `239`; crypto_major avg `0.6937` n `8`; equity avg `1.0102` n `166`; fx avg `0.0021` n `6`; index avg `0.1633` n `27`; metal avg `-0.0439` n `20`; unknown avg `0.5032` n `1084`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
