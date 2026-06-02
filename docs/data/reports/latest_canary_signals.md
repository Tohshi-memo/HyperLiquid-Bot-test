# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T14:52:30.971782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.4` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.6913` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5682` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.501` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.2372` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `0.0063` n `228`; crypto_major avg `-0.1278` n `8`; equity avg `0.2832` n `69`; fx avg `-0.0023` n `6`; index avg `0.1676` n `23`; metal avg `0.0567` n `18`; unknown avg `-0.0644` n `422`
- 1h: commodity avg `-0.0886` n `12`; crypto_alt avg `-1.6708` n `228`; crypto_major avg `-1.0952` n `8`; equity avg `0.4058` n `69`; fx avg `0.0315` n `6`; index avg `0.142` n `23`; metal avg `-0.0558` n `18`; unknown avg `-0.5984` n `422`
- 4h: commodity avg `0.0607` n `12`; crypto_alt avg `-1.4883` n `228`; crypto_major avg `-1.331` n `8`; equity avg `0.2372` n `69`; fx avg `0.0159` n `6`; index avg `0.3603` n `23`; metal avg `-0.3783` n `18`; unknown avg `-0.0664` n `422`
- 24h: commodity avg `-1.4454` n `12`; crypto_alt avg `-0.4776` n `228`; crypto_major avg `-1.5382` n `8`; equity avg `1.2224` n `69`; fx avg `0.2167` n `6`; index avg `0.7474` n `23`; metal avg `1.3117` n `18`; unknown avg `0.0096` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
