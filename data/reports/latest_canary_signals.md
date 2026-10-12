# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T18:37:31.287098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0384` n `13`; crypto_alt avg `-0.0749` n `235`; crypto_major avg `-0.094` n `8`; equity avg `-0.0321` n `151`; fx avg `-0.0051` n `6`; index avg `0.0006` n `26`; metal avg `-0.0054` n `20`; unknown avg `-0.2281` n `1134`
- 1h: commodity avg `0.0745` n `13`; crypto_alt avg `0.131` n `235`; crypto_major avg `0.0617` n `8`; equity avg `-0.0005` n `151`; fx avg `-0.005` n `6`; index avg `-0.0063` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.6244` n `1132`
- 4h: crypto_alt avg `-1.1316` n `227`; crypto_major avg `-1.0768` n `7`; metal avg `0.0264` n `1`; unknown avg `-0.2055` n `1033`
- 24h: commodity avg `0.5375` n `13`; crypto_alt avg `-3.0751` n `235`; crypto_major avg `-2.2918` n `8`; equity avg `-3.4998` n `151`; fx avg `-0.1707` n `6`; index avg `-0.3516` n `26`; metal avg `-0.1574` n `20`; unknown avg `-0.0341` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2146`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1857`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1278`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1245`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1004`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0857`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
