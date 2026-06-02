# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T18:07:28.445572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.48` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.9383` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.729` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1284` n `12`; crypto_alt avg `0.2074` n `228`; crypto_major avg `0.023` n `8`; equity avg `-0.0934` n `69`; fx avg `0.0012` n `6`; index avg `-0.0035` n `23`; metal avg `0.0488` n `18`; unknown avg `-0.076` n `422`
- 1h: commodity avg `0.0549` n `12`; crypto_alt avg `0.4393` n `228`; crypto_major avg `0.1741` n `8`; equity avg `-0.2214` n `69`; fx avg `-0.0067` n `6`; index avg `-0.1056` n `23`; metal avg `-0.1361` n `18`; unknown avg `-0.178` n `422`
- 4h: commodity avg `0.3398` n `12`; crypto_alt avg `-1.4893` n `228`; crypto_major avg `-1.6465` n `8`; equity avg `0.2918` n `69`; fx avg `-0.0075` n `6`; index avg `0.0825` n `23`; metal avg `-0.3102` n `18`; unknown avg `-0.4361` n `422`
- 24h: commodity avg `0.2101` n `12`; crypto_alt avg `-2.5589` n `228`; crypto_major avg `-3.2905` n `8`; equity avg `-0.3029` n `69`; fx avg `0.0705` n `6`; index avg `-0.0007` n `23`; metal avg `0.1108` n `18`; unknown avg `-0.5827` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
