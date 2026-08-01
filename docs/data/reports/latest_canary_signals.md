# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T14:07:27.297811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0645` n `12`; crypto_alt avg `0.0885` n `230`; crypto_major avg `0.0569` n `8`; equity avg `-0.0092` n `102`; fx avg `-0.0074` n `6`; index avg `-0.0013` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.0028` n `782`
- 1h: commodity avg `-0.0711` n `12`; crypto_alt avg `-0.0058` n `230`; crypto_major avg `0.0717` n `8`; equity avg `-0.0349` n `102`; fx avg `0.0044` n `6`; index avg `-0.0171` n `25`; metal avg `-0.0026` n `20`; unknown avg `-0.0734` n `782`
- 4h: commodity avg `-0.0145` n `12`; crypto_alt avg `0.3006` n `230`; crypto_major avg `0.1819` n `8`; equity avg `-0.0799` n `102`; fx avg `-0.0644` n `6`; index avg `-0.0247` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.1011` n `781`
- 24h: commodity avg `0.4375` n `12`; crypto_alt avg `1.1425` n `230`; crypto_major avg `-0.2612` n `8`; equity avg `-0.149` n `102`; fx avg `0.0573` n `6`; index avg `0.1001` n `25`; metal avg `0.2893` n `20`; unknown avg `4.4732` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
