# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T04:52:27.410619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.0358` n `233`; crypto_major avg `0.0078` n `8`; equity avg `-0.0099` n `136`; fx avg `-0.0025` n `6`; index avg `-0.0032` n `26`; metal avg `0.005` n `20`; unknown avg `-0.1626` n `838`
- 1h: commodity avg `0.0161` n `12`; crypto_alt avg `0.0797` n `233`; crypto_major avg `0.0089` n `8`; equity avg `-0.0493` n `136`; fx avg `0.0046` n `6`; index avg `-0.0122` n `26`; metal avg `0.001` n `20`; unknown avg `-0.1919` n `830`
- 4h: commodity avg `-0.0107` n `12`; crypto_alt avg `0.1744` n `233`; crypto_major avg `-0.1343` n `8`; equity avg `-0.1852` n `136`; fx avg `0.0066` n `6`; index avg `-0.0374` n `26`; metal avg `0.0032` n `20`; unknown avg `-0.2286` n `806`
- 24h: commodity avg `0.0799` n `12`; crypto_alt avg `0.9676` n `233`; crypto_major avg `-0.0003` n `8`; equity avg `-0.5136` n `136`; fx avg `-0.0078` n `6`; index avg `-0.0651` n `26`; metal avg `0.0398` n `20`; unknown avg `-0.3468` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
