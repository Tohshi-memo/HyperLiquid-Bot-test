# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T16:37:33.569326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `13`; crypto_alt avg `-0.182` n `235`; crypto_major avg `-0.0602` n `8`; equity avg `0.12` n `150`; fx avg `0.0026` n `6`; index avg `0.0056` n `26`; metal avg `-0.0213` n `20`; unknown avg `1.5687` n `1084`
- 1h: commodity avg `-0.1288` n `13`; crypto_alt avg `0.2073` n `235`; crypto_major avg `-0.078` n `8`; equity avg `0.0759` n `150`; fx avg `-0.0221` n `6`; index avg `0.0257` n `26`; metal avg `-0.0439` n `20`; unknown avg `1.4028` n `1050`
- 4h: commodity avg `0.3071` n `13`; crypto_alt avg `0.0997` n `235`; crypto_major avg `-0.5586` n `8`; equity avg `-0.3654` n `150`; fx avg `0.0047` n `6`; index avg `-0.0382` n `26`; metal avg `0.0164` n `20`; unknown avg `0.2393` n `996`
- 24h: commodity avg `0.2087` n `13`; crypto_alt avg `2.7644` n `235`; crypto_major avg `1.5097` n `8`; equity avg `0.0204` n `150`; fx avg `0.0353` n `6`; index avg `0.0078` n `26`; metal avg `0.6712` n `20`; unknown avg `1.3664` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
