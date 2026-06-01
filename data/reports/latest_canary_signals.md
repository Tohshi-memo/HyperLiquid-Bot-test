# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T16:52:30.332690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2049` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.7103` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.0346` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.3322` n `12`; crypto_alt avg `0.4823` n `228`; crypto_major avg `0.3152` n `8`; equity avg `0.3134` n `69`; fx avg `0.0078` n `6`; index avg `0.0893` n `23`; metal avg `0.1218` n `18`; unknown avg `0.9876` n `422`
- 1h: commodity avg `0.0061` n `12`; crypto_alt avg `1.0224` n `228`; crypto_major avg `0.5487` n `8`; equity avg `0.0075` n `69`; fx avg `0.0244` n `6`; index avg `0.1421` n `23`; metal avg `-0.021` n `18`; unknown avg `0.0007` n `422`
- 4h: commodity avg `1.1542` n `12`; crypto_alt avg `0.6995` n `228`; crypto_major avg `-1.0507` n `8`; equity avg `0.6596` n `69`; fx avg `0.0004` n `6`; index avg `-0.0161` n `23`; metal avg `-0.5839` n `18`; unknown avg `1.0587` n `422`
- 24h: commodity avg `1.0548` n `12`; crypto_alt avg `1.6489` n `228`; crypto_major avg `-0.7206` n `8`; equity avg `0.2419` n `69`; fx avg `0.0152` n `6`; index avg `0.3063` n `23`; metal avg `-0.149` n `18`; unknown avg `4.5714` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2875`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2178`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
