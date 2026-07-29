# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T09:37:30.313004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.86` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.086` n `12`; crypto_alt avg `0.0946` n `230`; crypto_major avg `0.1026` n `8`; equity avg `-0.0343` n `102`; fx avg `-0.0132` n `6`; index avg `-0.0101` n `25`; metal avg `-0.0188` n `20`; unknown avg `-0.0065` n `777`
- 1h: commodity avg `0.0727` n `12`; crypto_alt avg `0.2989` n `230`; crypto_major avg `0.3018` n `8`; equity avg `0.6328` n `102`; fx avg `0.0006` n `6`; index avg `0.1012` n `25`; metal avg `-0.0196` n `20`; unknown avg `0.0505` n `777`
- 4h: commodity avg `0.0578` n `12`; crypto_alt avg `0.3326` n `230`; crypto_major avg `0.4304` n `8`; equity avg `1.0012` n `102`; fx avg `0.0607` n `6`; index avg `0.2484` n `25`; metal avg `-0.0293` n `20`; unknown avg `-0.1946` n `761`
- 24h: commodity avg `0.1171` n `12`; crypto_alt avg `-1.0661` n `230`; crypto_major avg `1.1799` n `8`; equity avg `-0.8181` n `102`; fx avg `-0.096` n `6`; index avg `-0.1039` n `25`; metal avg `0.0317` n `20`; unknown avg `-0.5897` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
