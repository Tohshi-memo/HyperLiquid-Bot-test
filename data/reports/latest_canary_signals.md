# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T05:07:28.200477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `13`; crypto_alt avg `0.0852` n `235`; crypto_major avg `0.0274` n `8`; equity avg `0.009` n `150`; fx avg `-0.0001` n `6`; index avg `0.0035` n `26`; metal avg `-0.0078` n `20`; unknown avg `-0.0563` n `1114`
- 1h: commodity avg `0.0185` n `13`; crypto_alt avg `0.1164` n `235`; crypto_major avg `-0.001` n `8`; equity avg `-0.0012` n `150`; fx avg `-0.0005` n `6`; index avg `0.0091` n `26`; metal avg `-0.0155` n `20`; unknown avg `-0.2784` n `1114`
- 4h: commodity avg `0.003` n `13`; crypto_alt avg `0.6621` n `235`; crypto_major avg `0.2715` n `8`; equity avg `0.0498` n `150`; fx avg `0.0044` n `6`; index avg `0.0157` n `26`; metal avg `-0.0232` n `20`; unknown avg `-0.2101` n `1108`
- 24h: commodity avg `0.0631` n `13`; crypto_alt avg `2.0872` n `235`; crypto_major avg `0.2921` n `8`; equity avg `0.3099` n `150`; fx avg `-0.0186` n `6`; index avg `0.0546` n `26`; metal avg `0.1039` n `20`; unknown avg `12.5999` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
