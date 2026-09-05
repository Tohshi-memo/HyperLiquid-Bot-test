# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T13:37:31.874540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0583` n `12`; crypto_alt avg `-0.2439` n `232`; crypto_major avg `-0.1197` n `8`; equity avg `0.0084` n `134`; fx avg `-0.0` n `6`; index avg `-0.0131` n `26`; metal avg `0.0045` n `20`; unknown avg `0.2215` n `784`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `-0.0808` n `232`; crypto_major avg `0.3747` n `8`; equity avg `0.0094` n `134`; fx avg `0.0089` n `6`; index avg `-0.0019` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.0363` n `782`
- 4h: commodity avg `0.0515` n `12`; crypto_alt avg `0.1928` n `232`; crypto_major avg `0.7119` n `8`; equity avg `0.0663` n `134`; fx avg `0.0073` n `6`; index avg `0.0227` n `26`; metal avg `-0.0036` n `20`; unknown avg `-0.1429` n `772`
- 24h: commodity avg `0.4011` n `12`; crypto_alt avg `2.5745` n `232`; crypto_major avg `1.5467` n `8`; equity avg `0.9775` n `134`; fx avg `0.0582` n `6`; index avg `0.067` n `26`; metal avg `0.0945` n `20`; unknown avg `16.2245` n `692`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
