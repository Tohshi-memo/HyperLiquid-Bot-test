# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T09:37:25.687497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1602` n `13`; crypto_alt avg `0.0682` n `235`; crypto_major avg `-0.0173` n `8`; equity avg `-0.0015` n `150`; fx avg `-0.0012` n `6`; index avg `0.0033` n `26`; metal avg `-0.0001` n `20`; unknown avg `-0.0178` n `1117`
- 1h: commodity avg `-0.1675` n `13`; crypto_alt avg `0.1078` n `235`; crypto_major avg `0.0562` n `8`; equity avg `0.0108` n `150`; fx avg `-0.0171` n `6`; index avg `0.0149` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.0197` n `1115`
- 4h: commodity avg `-0.1741` n `13`; crypto_alt avg `-0.4024` n `235`; crypto_major avg `-0.0546` n `8`; equity avg `-0.0838` n `150`; fx avg `-0.0099` n `6`; index avg `-0.0294` n `26`; metal avg `0.0034` n `20`; unknown avg `0.604` n `1082`
- 24h: commodity avg `-0.0818` n `13`; crypto_alt avg `1.5463` n `235`; crypto_major avg `0.1114` n `8`; equity avg `-0.2207` n `150`; fx avg `-0.0328` n `6`; index avg `-0.0343` n `26`; metal avg `0.0693` n `20`; unknown avg `632.1413` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
