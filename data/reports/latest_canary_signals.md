# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T10:07:29.468803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1138` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0375` n `12`; crypto_alt avg `-0.0153` n `231`; crypto_major avg `0.1053` n `8`; equity avg `-0.0636` n `127`; fx avg `-0.0049` n `6`; index avg `-0.024` n `26`; metal avg `-0.0722` n `20`; unknown avg `-0.0135` n `792`
- 1h: commodity avg `0.0868` n `12`; crypto_alt avg `-0.0975` n `231`; crypto_major avg `0.3162` n `8`; equity avg `0.0213` n `127`; fx avg `0.0171` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0782` n `20`; unknown avg `0.0259` n `792`
- 4h: commodity avg `0.1356` n `12`; crypto_alt avg `1.7032` n `231`; crypto_major avg `1.9186` n `8`; equity avg `0.9122` n `127`; fx avg `-0.0002` n `6`; index avg `0.0941` n `26`; metal avg `-0.1952` n `20`; unknown avg `0.2948` n `791`
- 24h: commodity avg `0.5489` n `12`; crypto_alt avg `2.4729` n `231`; crypto_major avg `3.1867` n `8`; equity avg `2.0784` n `127`; fx avg `-0.0791` n `6`; index avg `0.2969` n `26`; metal avg `-0.4542` n `20`; unknown avg `0.5931` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
