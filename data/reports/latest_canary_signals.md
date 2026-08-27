# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T19:37:34.888037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.0304` n `231`; crypto_major avg `-0.0563` n `8`; equity avg `-0.0013` n `127`; fx avg `-0.0012` n `6`; index avg `0.0088` n `26`; metal avg `0.014` n `20`; unknown avg `0.0461` n `792`
- 1h: commodity avg `0.0017` n `12`; crypto_alt avg `0.1853` n `231`; crypto_major avg `0.4042` n `8`; equity avg `0.1839` n `127`; fx avg `0.0063` n `6`; index avg `0.0602` n `26`; metal avg `0.0751` n `20`; unknown avg `-0.0156` n `792`
- 4h: commodity avg `0.2471` n `12`; crypto_alt avg `-0.3578` n `231`; crypto_major avg `-0.0506` n `8`; equity avg `0.3024` n `127`; fx avg `0.0208` n `6`; index avg `0.0243` n `26`; metal avg `0.1956` n `20`; unknown avg `0.3525` n `792`
- 24h: commodity avg `0.4414` n `12`; crypto_alt avg `2.9866` n `231`; crypto_major avg `4.1165` n `8`; equity avg `1.4171` n `127`; fx avg `-0.0348` n `6`; index avg `0.1357` n `26`; metal avg `0.2283` n `20`; unknown avg `1.1158` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
