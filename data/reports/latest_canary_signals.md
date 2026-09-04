# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T15:52:25.104895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.6979` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.69` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.4793` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3955` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2687` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.1457` n `232`; crypto_major avg `0.0654` n `8`; equity avg `0.1043` n `133`; fx avg `-0.0028` n `6`; index avg `0.0303` n `26`; metal avg `0.0277` n `20`; unknown avg `0.097` n `793`
- 1h: commodity avg `-0.0434` n `12`; crypto_alt avg `0.89` n `232`; crypto_major avg `0.6583` n `8`; equity avg `0.2254` n `133`; fx avg `0.0036` n `6`; index avg `0.0453` n `26`; metal avg `0.153` n `20`; unknown avg `0.8158` n `779`
- 4h: commodity avg `0.1133` n `12`; crypto_alt avg `-1.7635` n `232`; crypto_major avg `-2.366` n `8`; equity avg `0.3319` n `133`; fx avg `-0.0855` n `6`; index avg `0.0295` n `26`; metal avg `-0.0973` n `20`; unknown avg `1.1066` n `725`
- 24h: commodity avg `0.0988` n `12`; crypto_alt avg `-1.4088` n `232`; crypto_major avg `-2.109` n `8`; equity avg `1.3144` n `133`; fx avg `-0.0632` n `6`; index avg `0.1689` n `26`; metal avg `-0.2241` n `20`; unknown avg `27.4514` n `686`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
