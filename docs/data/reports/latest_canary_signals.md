# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T21:52:31.876555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1111` n `13`; crypto_alt avg `-0.0592` n `235`; crypto_major avg `-0.0254` n `8`; equity avg `-0.0109` n `150`; fx avg `0.0039` n `6`; index avg `0.0011` n `26`; metal avg `0.0035` n `20`; unknown avg `0.8146` n `1101`
- 1h: commodity avg `0.1371` n `13`; crypto_alt avg `-0.0518` n `235`; crypto_major avg `-0.0717` n `8`; equity avg `0.0155` n `150`; fx avg `-0.0028` n `6`; index avg `-0.0045` n `26`; metal avg `0.0071` n `20`; unknown avg `0.6997` n `1093`
- 4h: commodity avg `0.1666` n `13`; crypto_alt avg `0.5775` n `235`; crypto_major avg `0.0592` n `8`; equity avg `0.0624` n `150`; fx avg `-0.0012` n `6`; index avg `0.0015` n `26`; metal avg `0.0125` n `20`; unknown avg `1.3068` n `991`
- 24h: commodity avg `0.0111` n `13`; crypto_alt avg `2.7244` n `235`; crypto_major avg `0.9785` n `8`; equity avg `0.2014` n `150`; fx avg `-0.0097` n `6`; index avg `0.007` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.6018` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
