# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T02:37:26.997775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0914` n `12`; crypto_alt avg `-0.2794` n `234`; crypto_major avg `-0.2484` n `8`; equity avg `-0.1202` n `141`; fx avg `-0.0148` n `6`; index avg `-0.0054` n `26`; metal avg `-0.11` n `20`; unknown avg `283.4835` n `962`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `-0.7262` n `234`; crypto_major avg `-0.6651` n `8`; equity avg `-0.5377` n `141`; fx avg `-0.0267` n `6`; index avg `-0.0809` n `26`; metal avg `-0.0773` n `20`; unknown avg `285.8785` n `954`
- 4h: commodity avg `-0.0513` n `12`; crypto_alt avg `-0.5061` n `234`; crypto_major avg `-0.6026` n `8`; equity avg `-1.1967` n `141`; fx avg `0.0797` n `6`; index avg `-0.0722` n `26`; metal avg `-0.4902` n `20`; unknown avg `55.1275` n `940`
- 24h: commodity avg `-0.4117` n `12`; crypto_alt avg `-0.5158` n `234`; crypto_major avg `-1.3192` n `8`; equity avg `-1.3061` n `141`; fx avg `0.0668` n `6`; index avg `-0.1311` n `26`; metal avg `-0.676` n `20`; unknown avg `11.7605` n `819`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
