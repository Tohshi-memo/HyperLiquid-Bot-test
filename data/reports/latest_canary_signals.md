# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T21:22:34.560533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0375` n `13`; crypto_alt avg `-0.1274` n `235`; crypto_major avg `-0.1141` n `8`; equity avg `-0.0339` n `150`; fx avg `-0.0002` n `6`; index avg `-0.0048` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.0255` n `1076`
- 1h: commodity avg `-0.0147` n `13`; crypto_alt avg `-0.3405` n `235`; crypto_major avg `-0.1708` n `8`; equity avg `0.0605` n `150`; fx avg `-0.0006` n `6`; index avg `0.0155` n `26`; metal avg `0.0028` n `20`; unknown avg `1.631` n `1066`
- 4h: commodity avg `0.2796` n `13`; crypto_alt avg `-0.2356` n `235`; crypto_major avg `-0.0534` n `8`; equity avg `-0.0152` n `150`; fx avg `0.0031` n `6`; index avg `-0.0173` n `26`; metal avg `0.0659` n `20`; unknown avg `0.9336` n `1006`
- 24h: commodity avg `0.2766` n `13`; crypto_alt avg `-1.5383` n `235`; crypto_major avg `-0.947` n `8`; equity avg `0.355` n `149`; fx avg `0.0885` n `6`; index avg `-0.0165` n `26`; metal avg `0.0402` n `20`; unknown avg `855.1063` n `930`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
