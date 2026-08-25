# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T19:05:29.986092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `-0.0214` n `231`; crypto_major avg `0.0141` n `8`; equity avg `-0.0142` n `122`; fx avg `-0.0037` n `6`; index avg `-0.014` n `25`; metal avg `0.0537` n `20`; unknown avg `0.0933` n `795`
- 1h: commodity avg `0.0851` n `12`; crypto_alt avg `0.0288` n `231`; crypto_major avg `-0.047` n `8`; equity avg `0.2539` n `122`; fx avg `0.0005` n `6`; index avg `0.0313` n `25`; metal avg `0.0606` n `20`; unknown avg `0.0586` n `795`
- 4h: commodity avg `0.0642` n `12`; crypto_alt avg `-0.039` n `231`; crypto_major avg `0.1691` n `8`; equity avg `0.2673` n `122`; fx avg `-0.0042` n `6`; index avg `0.0483` n `25`; metal avg `0.1908` n `20`; unknown avg `-0.1532` n `795`
- 24h: commodity avg `-0.5825` n `12`; crypto_alt avg `-0.0564` n `231`; crypto_major avg `1.1407` n `8`; equity avg `1.7252` n `122`; fx avg `0.0522` n `6`; index avg `0.1779` n `25`; metal avg `0.0313` n `20`; unknown avg `-0.535` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
