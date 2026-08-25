# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T23:52:24.706297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4933` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0122` n `12`; crypto_alt avg `-0.4189` n `231`; crypto_major avg `-0.4826` n `8`; equity avg `-0.1333` n `122`; fx avg `0.0005` n `6`; index avg `-0.0396` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.0996` n `796`
- 1h: commodity avg `0.0355` n `12`; crypto_alt avg `-0.7704` n `231`; crypto_major avg `-0.8266` n `8`; equity avg `-0.2834` n `122`; fx avg `-0.0067` n `6`; index avg `-0.0624` n `25`; metal avg `-0.0867` n `20`; unknown avg `-0.1429` n `795`
- 4h: commodity avg `-0.0837` n `12`; crypto_alt avg `-1.4111` n `231`; crypto_major avg `-1.5296` n `8`; equity avg `-0.1577` n `122`; fx avg `0.0043` n `6`; index avg `-0.0363` n `25`; metal avg `-0.0661` n `20`; unknown avg `-0.4721` n `795`
- 24h: commodity avg `-0.7027` n `12`; crypto_alt avg `-2.4128` n `231`; crypto_major avg `-1.6816` n `8`; equity avg `1.9896` n `122`; fx avg `0.0484` n `6`; index avg `0.2201` n `25`; metal avg `-0.2461` n `20`; unknown avg `-0.4553` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
