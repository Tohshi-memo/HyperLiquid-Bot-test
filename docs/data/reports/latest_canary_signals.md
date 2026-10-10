# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T02:07:29.044485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.038` n `13`; crypto_alt avg `0.1602` n `235`; crypto_major avg `-0.01` n `8`; equity avg `-0.0136` n `150`; fx avg `-0.0006` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0021` n `20`; unknown avg `-0.0306` n `1114`
- 1h: commodity avg `-0.0386` n `13`; crypto_alt avg `0.5027` n `235`; crypto_major avg `0.3001` n `8`; equity avg `-0.0059` n `150`; fx avg `-0.0024` n `6`; index avg `0.0045` n `26`; metal avg `-0.0198` n `20`; unknown avg `0.4145` n `1114`
- 4h: commodity avg `-0.0066` n `13`; crypto_alt avg `1.5759` n `235`; crypto_major avg `0.6374` n `8`; equity avg `0.0902` n `150`; fx avg `0.0014` n `6`; index avg `0.027` n `26`; metal avg `0.0128` n `20`; unknown avg `0.3812` n `1108`
- 24h: commodity avg `-0.0519` n `13`; crypto_alt avg `2.4523` n `235`; crypto_major avg `0.5564` n `8`; equity avg `0.4758` n `150`; fx avg `-0.0261` n `6`; index avg `0.0946` n `26`; metal avg `0.1992` n `20`; unknown avg `13.0997` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
