# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T14:07:34.427226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1966` n `13`; crypto_alt avg `0.7318` n `236`; crypto_major avg `0.568` n `8`; equity avg `0.6225` n `151`; fx avg `0.0528` n `6`; index avg `0.1284` n `26`; metal avg `0.0058` n `20`; unknown avg `1.3987` n `1098`
- 1h: commodity avg `0.1428` n `13`; crypto_alt avg `0.2827` n `236`; crypto_major avg `-0.0139` n `8`; equity avg `-0.1104` n `151`; fx avg `0.0507` n `6`; index avg `0.0689` n `26`; metal avg `-0.0162` n `20`; unknown avg `0.393` n `1098`
- 4h: commodity avg `0.1135` n `13`; crypto_alt avg `-0.4246` n `236`; crypto_major avg `-0.8173` n `8`; equity avg `-0.544` n `151`; fx avg `0.0488` n `6`; index avg `0.0579` n `26`; metal avg `-0.0783` n `20`; unknown avg `1.2949` n `1044`
- 24h: commodity avg `-0.1291` n `13`; crypto_alt avg `-3.0775` n `236`; crypto_major avg `-2.5567` n `8`; equity avg `-4.607` n `151`; fx avg `0.2267` n `6`; index avg `-0.6505` n `26`; metal avg `0.1063` n `20`; unknown avg `-0.3907` n `945`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1204`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0991`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0855`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.081`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0809`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0775`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
