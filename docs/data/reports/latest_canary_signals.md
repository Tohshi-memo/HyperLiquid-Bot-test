# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T03:07:24.826091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `13`; crypto_alt avg `-0.1908` n `235`; crypto_major avg `-0.0742` n `8`; equity avg `-0.0153` n `150`; fx avg `-0.0056` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.0621` n `1115`
- 1h: commodity avg `0.0353` n `13`; crypto_alt avg `-0.2417` n `235`; crypto_major avg `-0.0449` n `8`; equity avg `-0.0067` n `150`; fx avg `-0.0028` n `6`; index avg `-0.0015` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.2141` n `1115`
- 4h: commodity avg `0.0811` n `13`; crypto_alt avg `-0.0254` n `235`; crypto_major avg `-0.1365` n `8`; equity avg `-0.0351` n `150`; fx avg `0.0037` n `6`; index avg `0.0004` n `26`; metal avg `0.0077` n `20`; unknown avg `0.0256` n `1109`
- 24h: commodity avg `0.1429` n `13`; crypto_alt avg `0.9754` n `235`; crypto_major avg `0.2836` n `8`; equity avg `0.0701` n `150`; fx avg `-0.0105` n `6`; index avg `-0.0099` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.3616` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
