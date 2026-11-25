# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T02:37:33.326025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1749` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `0.1871` n `239`; crypto_major avg `0.1942` n `8`; equity avg `0.0592` n `168`; fx avg `-0.0186` n `6`; index avg `0.0178` n `27`; metal avg `-0.0078` n `20`; unknown avg `0.195` n `1265`
- 1h: commodity avg `-0.1712` n `13`; crypto_alt avg `-0.2053` n `239`; crypto_major avg `-0.4521` n `8`; equity avg `-0.9732` n `168`; fx avg `-0.0139` n `6`; index avg `-0.1201` n `27`; metal avg `0.0891` n `20`; unknown avg `-0.1097` n `1261`
- 4h: commodity avg `-0.1503` n `13`; crypto_alt avg `-0.8382` n `239`; crypto_major avg `-1.3632` n `8`; equity avg `-1.8203` n `168`; fx avg `0.0074` n `6`; index avg `-0.1883` n `27`; metal avg `0.0643` n `20`; unknown avg `0.2837` n `1173`
- 24h: commodity avg `0.5638` n `13`; crypto_alt avg `-3.3039` n `239`; crypto_major avg `-2.9491` n `8`; equity avg `-5.2718` n `167`; fx avg `0.1879` n `6`; index avg `-0.5602` n `27`; metal avg `-0.9594` n `20`; unknown avg `487.299` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
