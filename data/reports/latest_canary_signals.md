# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T14:22:29.228756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.38` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.2743` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.1144` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0649` n `12`; crypto_alt avg `-1.0142` n `228`; crypto_major avg `-0.6874` n `8`; equity avg `0.0307` n `69`; fx avg `-0.0016` n `6`; index avg `0.0329` n `23`; metal avg `-0.3053` n `18`; unknown avg `1.0678` n `422`
- 1h: commodity avg `0.4052` n `12`; crypto_alt avg `-1.3891` n `228`; crypto_major avg `-1.0087` n `8`; equity avg `-0.098` n `69`; fx avg `-0.0369` n `6`; index avg `0.2656` n `23`; metal avg `-0.4148` n `18`; unknown avg `1.2027` n `422`
- 4h: commodity avg `0.1101` n `12`; crypto_alt avg `-0.7216` n `228`; crypto_major avg `-0.893` n `8`; equity avg `-0.1307` n `69`; fx avg `-0.0092` n `6`; index avg `0.2214` n `23`; metal avg `-0.6433` n `18`; unknown avg `1.7229` n `422`
- 24h: commodity avg `-1.0279` n `12`; crypto_alt avg `-0.0484` n `228`; crypto_major avg `-1.3886` n `8`; equity avg `1.1196` n `69`; fx avg `0.1858` n `6`; index avg `0.6295` n `23`; metal avg `0.9419` n `18`; unknown avg `1.02` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
