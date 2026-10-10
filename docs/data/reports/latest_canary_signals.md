# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T04:22:29.696931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `13`; crypto_alt avg `-0.1459` n `235`; crypto_major avg `-0.1054` n `8`; equity avg `-0.0091` n `150`; fx avg `-0.0007` n `6`; index avg `0.0022` n `26`; metal avg `-0.006` n `20`; unknown avg `-0.1611` n `1116`
- 1h: commodity avg `0.0155` n `13`; crypto_alt avg `-0.0789` n `235`; crypto_major avg `0.0182` n `8`; equity avg `0.0244` n `150`; fx avg `0.0047` n `6`; index avg `0.0067` n `26`; metal avg `-0.0067` n `20`; unknown avg `-0.2344` n `1108`
- 4h: commodity avg `-0.0245` n `13`; crypto_alt avg `0.2572` n `235`; crypto_major avg `0.1329` n `8`; equity avg `0.0758` n `150`; fx avg `0.0078` n `6`; index avg `0.0226` n `26`; metal avg `0.0029` n `20`; unknown avg `-0.147` n `1108`
- 24h: commodity avg `0.0534` n `13`; crypto_alt avg `1.7023` n `235`; crypto_major avg `-0.0027` n `8`; equity avg `0.3724` n `150`; fx avg `-0.0195` n `6`; index avg `0.0606` n `26`; metal avg `0.1333` n `20`; unknown avg `12.856` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
