# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T11:52:23.270148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `0.0999` n `231`; crypto_major avg `0.0311` n `8`; equity avg `0.0071` n `128`; fx avg `0.0012` n `6`; index avg `-0.0083` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.0005` n `793`
- 1h: commodity avg `-0.0107` n `12`; crypto_alt avg `-0.0128` n `231`; crypto_major avg `-0.0381` n `8`; equity avg `0.033` n `128`; fx avg `0.0029` n `6`; index avg `0.0115` n `26`; metal avg `0.0026` n `20`; unknown avg `-0.0755` n `791`
- 4h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.6269` n `231`; crypto_major avg `0.0958` n `8`; equity avg `0.0469` n `128`; fx avg `0.0031` n `6`; index avg `0.0077` n `26`; metal avg `0.0007` n `20`; unknown avg `-0.3516` n `789`
- 24h: commodity avg `-0.0323` n `12`; crypto_alt avg `1.5947` n `231`; crypto_major avg `0.8966` n `8`; equity avg `0.2818` n `128`; fx avg `0.0144` n `6`; index avg `0.061` n `26`; metal avg `0.091` n `20`; unknown avg `-0.1823` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
