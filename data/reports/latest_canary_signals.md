# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T01:52:27.816716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `13`; crypto_alt avg `0.1324` n `235`; crypto_major avg `-0.0279` n `8`; equity avg `0.0152` n `150`; fx avg `0.0019` n `6`; index avg `0.0018` n `26`; metal avg `0.0019` n `20`; unknown avg `2.9087` n `1117`
- 1h: commodity avg `-0.03` n `13`; crypto_alt avg `0.686` n `235`; crypto_major avg `0.2147` n `8`; equity avg `0.0225` n `150`; fx avg `0.0005` n `6`; index avg `-0.0039` n `26`; metal avg `0.0025` n `20`; unknown avg `1.5169` n `1115`
- 4h: commodity avg `0.0479` n `13`; crypto_alt avg `0.1149` n `235`; crypto_major avg `-0.0939` n `8`; equity avg `-0.0183` n `150`; fx avg `0.004` n `6`; index avg `0.0002` n `26`; metal avg `0.0069` n `20`; unknown avg `4.4816` n `1101`
- 24h: commodity avg `0.0481` n `13`; crypto_alt avg `1.5945` n `235`; crypto_major avg `0.2816` n `8`; equity avg `0.0874` n `150`; fx avg `-0.0078` n `6`; index avg `-0.0161` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.3669` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
