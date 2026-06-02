# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T07:07:21.010774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.74` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-3.0898` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.6918` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.3483` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0641` n `12`; crypto_alt avg `-0.3038` n `228`; crypto_major avg `-0.2789` n `8`; equity avg `-0.047` n `69`; fx avg `-0.0177` n `6`; index avg `0.0697` n `23`; metal avg `0.1147` n `18`; unknown avg `-0.1972` n `422`
- 1h: commodity avg `0.1438` n `12`; crypto_alt avg `-0.5731` n `228`; crypto_major avg `-0.6763` n `8`; equity avg `0.0404` n `69`; fx avg `0.0626` n `6`; index avg `0.067` n `23`; metal avg `0.198` n `18`; unknown avg `-0.305` n `422`
- 4h: commodity avg `-0.2323` n `12`; crypto_alt avg `-1.3242` n `228`; crypto_major avg `-1.9175` n `8`; equity avg `0.7743` n `69`; fx avg `0.0709` n `6`; index avg `0.4308` n `23`; metal avg `1.1723` n `18`; unknown avg `0.3841` n `412`
- 24h: commodity avg `-0.9153` n `12`; crypto_alt avg `-0.9719` n `228`; crypto_major avg `-2.2436` n `8`; equity avg `0.0538` n `69`; fx avg `0.1424` n `6`; index avg `-0.5907` n `23`; metal avg `1.2031` n `18`; unknown avg `2.5618` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.193`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
