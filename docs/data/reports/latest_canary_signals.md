# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T17:37:28.471772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `12`; crypto_alt avg `-0.0381` n `231`; crypto_major avg `-0.0129` n `8`; equity avg `-0.0614` n `122`; fx avg `0.0039` n `6`; index avg `-0.0097` n `25`; metal avg `-0.0134` n `20`; unknown avg `0.0349` n `795`
- 1h: commodity avg `-0.0141` n `12`; crypto_alt avg `-0.3948` n `231`; crypto_major avg `-0.2473` n `8`; equity avg `-0.1886` n `122`; fx avg `0.0078` n `6`; index avg `-0.037` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.2152` n `795`
- 4h: commodity avg `0.1072` n `12`; crypto_alt avg `-0.3881` n `231`; crypto_major avg `-0.0161` n `8`; equity avg `0.0219` n `122`; fx avg `-0.0167` n `6`; index avg `-0.0787` n `25`; metal avg `0.2772` n `20`; unknown avg `-0.2024` n `795`
- 24h: commodity avg `-0.5954` n `12`; crypto_alt avg `-0.2785` n `231`; crypto_major avg `0.9051` n `8`; equity avg `1.6664` n `122`; fx avg `0.0576` n `6`; index avg `0.208` n `25`; metal avg `-0.0807` n `20`; unknown avg `-0.715` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
