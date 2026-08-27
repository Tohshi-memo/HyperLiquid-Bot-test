# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T15:22:49.633963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.7454` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.1576` n `231`; crypto_major avg `0.1096` n `8`; equity avg `-0.0989` n `127`; fx avg `0.0047` n `6`; index avg `-0.0104` n `26`; metal avg `0.003` n `20`; unknown avg `0.0035` n `792`
- 1h: commodity avg `-0.2716` n `12`; crypto_alt avg `0.2061` n `231`; crypto_major avg `0.4869` n `8`; equity avg `-0.3715` n `127`; fx avg `-0.0178` n `6`; index avg `-0.0137` n `26`; metal avg `0.0518` n `20`; unknown avg `-0.0835` n `792`
- 4h: commodity avg `0.0169` n `12`; crypto_alt avg `0.8754` n `231`; crypto_major avg `1.1315` n `8`; equity avg `-0.6139` n `127`; fx avg `0.0221` n `6`; index avg `-0.0635` n `26`; metal avg `0.0336` n `20`; unknown avg `-0.0981` n `792`
- 24h: commodity avg `0.1696` n `12`; crypto_alt avg `3.586` n `231`; crypto_major avg `4.4579` n `8`; equity avg `1.5406` n `127`; fx avg `-0.054` n `6`; index avg `0.158` n `26`; metal avg `-0.1361` n `20`; unknown avg `0.7888` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
