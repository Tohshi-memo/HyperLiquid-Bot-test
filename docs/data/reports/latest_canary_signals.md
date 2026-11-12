# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T10:07:29.778689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `13`; crypto_alt avg `-0.013` n `239`; crypto_major avg `0.0728` n `8`; equity avg `0.0232` n `162`; fx avg `-0.0008` n `6`; index avg `0.0026` n `27`; metal avg `-0.0216` n `20`; unknown avg `0.1969` n `1257`
- 1h: commodity avg `-0.1798` n `13`; crypto_alt avg `0.2445` n `239`; crypto_major avg `0.3181` n `8`; equity avg `0.5226` n `162`; fx avg `-0.0226` n `6`; index avg `0.0522` n `27`; metal avg `0.0365` n `20`; unknown avg `0.6089` n `1255`
- 4h: commodity avg `-0.0082` n `13`; crypto_alt avg `0.0306` n `239`; crypto_major avg `0.1332` n `8`; equity avg `0.7968` n `162`; fx avg `0.0758` n `6`; index avg `0.0542` n `27`; metal avg `-0.2057` n `20`; unknown avg `56.4824` n `1231`
- 24h: commodity avg `-0.0376` n `13`; crypto_alt avg `-1.517` n `239`; crypto_major avg `-0.5742` n `8`; equity avg `-0.4767` n `162`; fx avg `-0.0882` n `6`; index avg `-0.0178` n `27`; metal avg `-0.9372` n `20`; unknown avg `17.8082` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
