# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T23:07:27.214741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `0.0635` n `235`; crypto_major avg `-0.0362` n `8`; equity avg `0.0107` n `150`; fx avg `0.0` n `6`; index avg `-0.0014` n `26`; metal avg `0.0016` n `20`; unknown avg `0.0067` n `1114`
- 1h: commodity avg `0.007` n `13`; crypto_alt avg `0.4734` n `235`; crypto_major avg `0.1898` n `8`; equity avg `0.0306` n `150`; fx avg `-0.0037` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.1867` n `1114`
- 4h: commodity avg `-0.0382` n `13`; crypto_alt avg `0.7912` n `235`; crypto_major avg `0.1843` n `8`; equity avg `0.0538` n `150`; fx avg `-0.0128` n `6`; index avg `-0.0139` n `26`; metal avg `-0.0646` n `20`; unknown avg `0.2372` n `1026`
- 24h: commodity avg `-0.1244` n `13`; crypto_alt avg `2.0442` n `235`; crypto_major avg `0.3753` n `8`; equity avg `0.7816` n `150`; fx avg `0.0041` n `6`; index avg `0.1234` n `26`; metal avg `0.5387` n `20`; unknown avg `12.8194` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
