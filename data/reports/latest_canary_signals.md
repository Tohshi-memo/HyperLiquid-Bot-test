# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T09:52:32.068821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `13`; crypto_alt avg `0.0563` n `239`; crypto_major avg `-0.0235` n `8`; equity avg `0.0547` n `158`; fx avg `-0.0118` n `6`; index avg `0.0142` n `27`; metal avg `-0.0016` n `20`; unknown avg `201.0768` n `1246`
- 1h: commodity avg `0.0231` n `13`; crypto_alt avg `-0.1543` n `239`; crypto_major avg `-0.0871` n `8`; equity avg `0.1167` n `158`; fx avg `0.0034` n `6`; index avg `-0.0119` n `27`; metal avg `0.0055` n `20`; unknown avg `212.9798` n `1176`
- 4h: commodity avg `0.0526` n `13`; crypto_alt avg `-0.161` n `239`; crypto_major avg `-0.0417` n `8`; equity avg `0.2029` n `158`; fx avg `-0.0046` n `6`; index avg `-0.0008` n `27`; metal avg `0.0147` n `20`; unknown avg `219.2375` n `1140`
- 24h: commodity avg `0.1289` n `13`; crypto_alt avg `-1.4753` n `239`; crypto_major avg `-0.6082` n `8`; equity avg `0.124` n `158`; fx avg `0.0491` n `6`; index avg `0.0109` n `27`; metal avg `-0.0257` n `20`; unknown avg `-0.1927` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
