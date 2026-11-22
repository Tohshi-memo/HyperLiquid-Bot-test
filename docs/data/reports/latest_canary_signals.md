# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T20:52:26.639882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `13`; crypto_alt avg `0.0411` n `239`; crypto_major avg `0.2023` n `8`; equity avg `0.0543` n `166`; fx avg `-0.0022` n `6`; index avg `0.0034` n `27`; metal avg `0.0047` n `20`; unknown avg `262.7015` n `1264`
- 1h: commodity avg `0.007` n `13`; crypto_alt avg `0.1348` n `239`; crypto_major avg `0.1136` n `8`; equity avg `0.0228` n `166`; fx avg `-0.008` n `6`; index avg `-0.0123` n `27`; metal avg `-0.0219` n `20`; unknown avg `12.1129` n `1252`
- 4h: commodity avg `-0.0298` n `13`; crypto_alt avg `-0.354` n `239`; crypto_major avg `-0.3687` n `8`; equity avg `0.0823` n `166`; fx avg `-0.0015` n `6`; index avg `-0.0189` n `27`; metal avg `-0.084` n `20`; unknown avg `45.3239` n `1231`
- 24h: commodity avg `-0.1162` n `13`; crypto_alt avg `0.6043` n `239`; crypto_major avg `0.5353` n `8`; equity avg `0.8737` n `166`; fx avg `-0.0107` n `6`; index avg `0.0956` n `27`; metal avg `-0.0359` n `20`; unknown avg `188.9676` n `1056`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
