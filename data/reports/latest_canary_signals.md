# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T01:22:30.244029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.0732` n `232`; crypto_major avg `-0.0852` n `8`; equity avg `0.035` n `130`; fx avg `0.0161` n `6`; index avg `0.0113` n `26`; metal avg `-0.0212` n `20`; unknown avg `1.4822` n `792`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.1247` n `232`; crypto_major avg `-0.2453` n `8`; equity avg `0.1362` n `130`; fx avg `0.0653` n `6`; index avg `0.0654` n `26`; metal avg `-0.0247` n `20`; unknown avg `3.4605` n `790`
- 4h: commodity avg `0.0665` n `12`; crypto_alt avg `0.6839` n `232`; crypto_major avg `-0.1332` n `8`; equity avg `0.1926` n `130`; fx avg `0.0426` n `6`; index avg `0.0624` n `26`; metal avg `0.0914` n `20`; unknown avg `3.4643` n `790`
- 24h: commodity avg `0.4776` n `12`; crypto_alt avg `2.0471` n `231`; crypto_major avg `1.6927` n `8`; equity avg `1.5708` n `130`; fx avg `-0.0339` n `6`; index avg `0.2571` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.2049` n `739`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
