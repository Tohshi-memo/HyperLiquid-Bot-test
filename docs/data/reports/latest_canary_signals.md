# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T14:52:29.012592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `13`; crypto_alt avg `0.026` n `235`; crypto_major avg `-0.0838` n `8`; equity avg `-0.0078` n `150`; fx avg `0.0149` n `6`; index avg `0.0113` n `26`; metal avg `-0.0123` n `20`; unknown avg `1.4914` n `1078`
- 1h: commodity avg `0.1458` n `13`; crypto_alt avg `0.2545` n `235`; crypto_major avg `0.2231` n `8`; equity avg `0.2512` n `150`; fx avg `0.0332` n `6`; index avg `0.0239` n `26`; metal avg `-0.1029` n `20`; unknown avg `0.0854` n `1070`
- 4h: commodity avg `0.4409` n `13`; crypto_alt avg `0.3137` n `235`; crypto_major avg `0.2844` n `8`; equity avg `-0.3726` n `150`; fx avg `-0.0067` n `6`; index avg `-0.048` n `26`; metal avg `0.0727` n `20`; unknown avg `0.9349` n `1022`
- 24h: commodity avg `-0.0229` n `13`; crypto_alt avg `-1.5714` n `235`; crypto_major avg `-1.2326` n `8`; equity avg `-0.5281` n `150`; fx avg `0.0036` n `6`; index avg `-0.029` n `26`; metal avg `0.6092` n `20`; unknown avg `30.1349` n `955`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
