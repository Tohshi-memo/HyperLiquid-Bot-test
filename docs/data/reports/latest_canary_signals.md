# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T23:07:23.508392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `13`; crypto_alt avg `0.0017` n `235`; crypto_major avg `0.0227` n `8`; equity avg `-0.0003` n `150`; fx avg `-0.0019` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0009` n `20`; unknown avg `-0.0057` n `1115`
- 1h: commodity avg `-0.1338` n `13`; crypto_alt avg `-0.1682` n `235`; crypto_major avg `0.0163` n `8`; equity avg `-0.0153` n `150`; fx avg `-0.0033` n `6`; index avg `-0.0038` n `26`; metal avg `-0.0082` n `20`; unknown avg `2.516` n `1107`
- 4h: commodity avg `0.1572` n `13`; crypto_alt avg `0.1713` n `235`; crypto_major avg `0.0556` n `8`; equity avg `0.0605` n `150`; fx avg `-0.0048` n `6`; index avg `0.0112` n `26`; metal avg `0.005` n `20`; unknown avg `2.3353` n `1055`
- 24h: commodity avg `0.0465` n `13`; crypto_alt avg `2.12` n `235`; crypto_major avg `0.8288` n `8`; equity avg `0.1852` n `150`; fx avg `-0.0109` n `6`; index avg `0.0173` n `26`; metal avg `0.0061` n `20`; unknown avg `0.2004` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
