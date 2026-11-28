# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T23:07:33.040054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `13`; crypto_alt avg `0.087` n `239`; crypto_major avg `0.1215` n `8`; equity avg `-0.0014` n `168`; fx avg `0.002` n `6`; index avg `-0.0084` n `27`; metal avg `0.0101` n `20`; unknown avg `74.6303` n `1246`
- 1h: commodity avg `0.0027` n `13`; crypto_alt avg `0.2515` n `239`; crypto_major avg `0.327` n `8`; equity avg `0.0471` n `168`; fx avg `0.0025` n `6`; index avg `0.0106` n `27`; metal avg `0.0007` n `20`; unknown avg `0.1068` n `1232`
- 4h: commodity avg `0.1427` n `13`; crypto_alt avg `0.0516` n `239`; crypto_major avg `0.1872` n `8`; equity avg `0.1208` n `168`; fx avg `-0.0178` n `6`; index avg `0.0172` n `27`; metal avg `0.0246` n `20`; unknown avg `-0.2001` n `1164`
- 24h: commodity avg `0.0689` n `13`; crypto_alt avg `-3.2761` n `239`; crypto_major avg `-0.8751` n `8`; equity avg `0.0621` n `168`; fx avg `0.0007` n `6`; index avg `0.0048` n `27`; metal avg `0.0289` n `20`; unknown avg `0.3479` n `1067`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
