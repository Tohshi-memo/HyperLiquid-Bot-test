# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T11:52:19.359530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.1736` n `228`; crypto_major avg `-0.1281` n `8`; equity avg `-0.1368` n `66`; fx avg `-0.005` n `6`; index avg `-0.0619` n `23`; metal avg `0.0323` n `18`; unknown avg `0.1077` n `383`
- 1h: commodity avg `0.2444` n `12`; crypto_alt avg `-0.2881` n `228`; crypto_major avg `-0.1892` n `8`; equity avg `-0.1301` n `66`; fx avg `-0.0304` n `6`; index avg `-0.0011` n `23`; metal avg `0.0732` n `18`; unknown avg `-0.2146` n `383`
- 4h: commodity avg `0.4069` n `12`; crypto_alt avg `-1.4035` n `228`; crypto_major avg `-0.8718` n `8`; equity avg `-1.0818` n `66`; fx avg `-0.0709` n `6`; index avg `-0.5704` n `23`; metal avg `-0.3666` n `18`; unknown avg `-0.6148` n `383`
- 24h: commodity avg `1.3868` n `12`; crypto_alt avg `0.3086` n `228`; crypto_major avg `-0.0015` n `8`; equity avg `-1.9103` n `66`; fx avg `0.2212` n `6`; index avg `-0.8411` n `23`; metal avg `-0.6038` n `18`; unknown avg `0.4638` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
