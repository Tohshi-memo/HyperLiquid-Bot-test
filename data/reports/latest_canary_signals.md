# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T00:52:20.757300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0381` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.0047` n `228`; crypto_major avg `-0.0288` n `8`; equity avg `-0.1387` n `73`; fx avg `-0.013` n `6`; index avg `-0.054` n `23`; metal avg `0.1272` n `18`; unknown avg `-0.1064` n `419`
- 1h: commodity avg `-0.041` n `12`; crypto_alt avg `-0.8571` n `228`; crypto_major avg `-0.9173` n `8`; equity avg `0.4915` n `73`; fx avg `-0.0321` n `6`; index avg `0.1208` n `23`; metal avg `-0.0396` n `18`; unknown avg `-0.4255` n `419`
- 4h: commodity avg `-0.2996` n `12`; crypto_alt avg `-0.1701` n `228`; crypto_major avg `-0.4067` n `8`; equity avg `-0.4842` n `73`; fx avg `-0.0668` n `6`; index avg `-0.1751` n `23`; metal avg `0.4343` n `18`; unknown avg `-0.0361` n `419`
- 24h: commodity avg `0.3889` n `12`; crypto_alt avg `0.0187` n `228`; crypto_major avg `-2.6709` n `8`; equity avg `-3.5657` n `72`; fx avg `-0.0094` n `6`; index avg `-1.0967` n `23`; metal avg `-2.0461` n `18`; unknown avg `0.5679` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
