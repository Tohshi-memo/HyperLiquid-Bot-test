# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T05:37:29.794384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0991` n `12`; crypto_alt avg `-0.1729` n `230`; crypto_major avg `-0.2246` n `8`; equity avg `-0.1657` n `102`; fx avg `-0.0101` n `6`; index avg `-0.0502` n `25`; metal avg `-0.0756` n `20`; unknown avg `-0.1751` n `774`
- 1h: commodity avg `0.0523` n `12`; crypto_alt avg `0.1442` n `230`; crypto_major avg `0.0446` n `8`; equity avg `-0.2534` n `102`; fx avg `-0.0344` n `6`; index avg `-0.072` n `25`; metal avg `-0.1424` n `20`; unknown avg `1.7858` n `774`
- 4h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.2248` n `230`; crypto_major avg `-0.0346` n `8`; equity avg `-0.9462` n `102`; fx avg `-0.0959` n `6`; index avg `-0.1952` n `25`; metal avg `-0.1687` n `20`; unknown avg `-0.3921` n `774`
- 24h: commodity avg `-0.7172` n `12`; crypto_alt avg `-3.8971` n `230`; crypto_major avg `-3.5307` n `8`; equity avg `-3.8625` n `102`; fx avg `-0.1572` n `6`; index avg `-0.892` n `25`; metal avg `-0.4044` n `20`; unknown avg `1161.8142` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
