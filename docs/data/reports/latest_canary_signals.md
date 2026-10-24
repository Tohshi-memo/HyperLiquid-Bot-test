# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T14:37:42.751383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `0.1601` n `237`; crypto_major avg `0.1215` n `8`; equity avg `0.135` n `152`; fx avg `-0.0028` n `6`; index avg `0.0131` n `26`; metal avg `-0.0071` n `20`; unknown avg `0.6612` n `1228`
- 1h: commodity avg `0.0193` n `13`; crypto_alt avg `-0.509` n `237`; crypto_major avg `-0.3737` n `8`; equity avg `-0.1652` n `152`; fx avg `-0.0063` n `6`; index avg `-0.0382` n `26`; metal avg `-0.0648` n `20`; unknown avg `2.0299` n `1228`
- 4h: commodity avg `0.1424` n `13`; crypto_alt avg `-1.2423` n `237`; crypto_major avg `-0.4873` n `8`; equity avg `-0.1637` n `152`; fx avg `-0.0206` n `6`; index avg `-0.0354` n `26`; metal avg `-0.0614` n `20`; unknown avg `0.9018` n `1190`
- 24h: commodity avg `0.214` n `13`; crypto_alt avg `-3.3737` n `237`; crypto_major avg `-2.4815` n `8`; equity avg `-0.6356` n `152`; fx avg `-0.0453` n `6`; index avg `-0.0261` n `26`; metal avg `-0.115` n `20`; unknown avg `-0.5731` n `1043`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1917`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
