# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T16:22:27.333940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2194` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0381` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0609` n `12`; crypto_alt avg `-0.6198` n `228`; crypto_major avg `-0.7119` n `8`; equity avg `-0.0213` n `73`; fx avg `0.0002` n `6`; index avg `-0.0144` n `23`; metal avg `0.0026` n `18`; unknown avg `0.7509` n `419`
- 1h: commodity avg `0.2966` n `12`; crypto_alt avg `-1.5416` n `228`; crypto_major avg `-1.1611` n `8`; equity avg `-0.4467` n `73`; fx avg `0.0113` n `6`; index avg `-0.123` n `23`; metal avg `-0.2271` n `18`; unknown avg `-0.366` n `419`
- 4h: commodity avg `-0.192` n `12`; crypto_alt avg `-0.9869` n `228`; crypto_major avg `-1.8271` n `8`; equity avg `-2.2004` n `73`; fx avg `0.0203` n `6`; index avg `-0.6077` n `23`; metal avg `-1.1001` n `18`; unknown avg `-0.078` n `419`
- 24h: commodity avg `1.0644` n `12`; crypto_alt avg `-0.2064` n `228`; crypto_major avg `-3.3991` n `8`; equity avg `-2.1312` n `72`; fx avg `0.0152` n `6`; index avg `-0.2487` n `23`; metal avg `-2.0955` n `18`; unknown avg `0.0541` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
