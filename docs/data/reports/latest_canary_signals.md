# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T18:37:32.024642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0483` n `12`; crypto_alt avg `-0.0189` n `234`; crypto_major avg `-0.1121` n `8`; equity avg `-0.0602` n `141`; fx avg `-0.0047` n `6`; index avg `-0.0175` n `26`; metal avg `0.014` n `20`; unknown avg `0.0561` n `960`
- 1h: commodity avg `-0.0381` n `12`; crypto_alt avg `0.7043` n `234`; crypto_major avg `0.5409` n `8`; equity avg `-0.0095` n `141`; fx avg `-0.0093` n `6`; index avg `0.0112` n `26`; metal avg `0.0595` n `20`; unknown avg `1.7443` n `958`
- 4h: commodity avg `-0.1918` n `12`; crypto_alt avg `0.6644` n `234`; crypto_major avg `0.0184` n `8`; equity avg `0.3737` n `141`; fx avg `-0.0451` n `6`; index avg `0.1421` n `26`; metal avg `0.2208` n `20`; unknown avg `4.1065` n `930`
- 24h: commodity avg `-0.8084` n `12`; crypto_alt avg `2.418` n `234`; crypto_major avg `0.7106` n `8`; equity avg `0.1767` n `141`; fx avg `-0.2563` n `6`; index avg `0.2147` n `26`; metal avg `0.166` n `20`; unknown avg `1594.0736` n `807`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
