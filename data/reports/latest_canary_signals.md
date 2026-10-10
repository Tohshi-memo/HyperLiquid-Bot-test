# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T13:52:29.026963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `13`; crypto_alt avg `0.0221` n `235`; crypto_major avg `0.0169` n `8`; equity avg `-0.0002` n `150`; fx avg `0.0` n `6`; index avg `0.001` n `26`; metal avg `0.004` n `20`; unknown avg `0.0705` n `1117`
- 1h: commodity avg `-0.0119` n `13`; crypto_alt avg `0.1903` n `235`; crypto_major avg `0.0966` n `8`; equity avg `0.015` n `150`; fx avg `-0.0078` n `6`; index avg `-0.0045` n `26`; metal avg `0.008` n `20`; unknown avg `0.4963` n `1115`
- 4h: commodity avg `0.0605` n `13`; crypto_alt avg `0.1294` n `235`; crypto_major avg `-0.0166` n `8`; equity avg `0.0361` n `150`; fx avg `0.0` n `6`; index avg `-0.0111` n `26`; metal avg `0.0079` n `20`; unknown avg `0.8425` n `1109`
- 24h: commodity avg `-0.3935` n `13`; crypto_alt avg `2.2891` n `235`; crypto_major avg `0.5164` n `8`; equity avg `0.5502` n `150`; fx avg `0.0226` n `6`; index avg `0.0605` n `26`; metal avg `-0.0718` n `20`; unknown avg `11.6727` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
