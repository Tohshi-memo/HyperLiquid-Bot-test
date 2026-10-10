# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T10:22:29.749110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `-0.086` n `235`; crypto_major avg `-0.0634` n `8`; equity avg `-0.0165` n `150`; fx avg `-0.001` n `6`; index avg `0.0` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.0854` n `1117`
- 1h: commodity avg `-0.2241` n `13`; crypto_alt avg `-0.2274` n `235`; crypto_major avg `-0.2553` n `8`; equity avg `-0.0205` n `150`; fx avg `-0.0018` n `6`; index avg `0.007` n `26`; metal avg `0.0055` n `20`; unknown avg `0.5261` n `1115`
- 4h: commodity avg `-0.2549` n `13`; crypto_alt avg `-0.4458` n `235`; crypto_major avg `-0.1406` n `8`; equity avg `-0.0643` n `150`; fx avg `-0.0105` n `6`; index avg `-0.0221` n `26`; metal avg `0.0072` n `20`; unknown avg `1.8065` n `1098`
- 24h: commodity avg `-0.1149` n `13`; crypto_alt avg `1.2373` n `235`; crypto_major avg `-0.0319` n `8`; equity avg `-0.225` n `150`; fx avg `-0.0243` n `6`; index avg `-0.0165` n `26`; metal avg `0.0652` n `20`; unknown avg `632.2908` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
