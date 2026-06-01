# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T15:52:25.647762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.1868` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.0884` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4746` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2062` n `12`; crypto_alt avg `-0.0657` n `228`; crypto_major avg `-0.4023` n `8`; equity avg `-0.0454` n `69`; fx avg `0.0299` n `6`; index avg `-0.0536` n `23`; metal avg `-0.166` n `18`; unknown avg `0.7796` n `422`
- 1h: commodity avg `-0.3886` n `12`; crypto_alt avg `0.5032` n `228`; crypto_major avg `-0.0214` n `8`; equity avg `0.8978` n `69`; fx avg `0.053` n `6`; index avg `0.156` n `23`; metal avg `0.543` n `18`; unknown avg `1.0564` n `422`
- 4h: commodity avg `0.4029` n `12`; crypto_alt avg `-0.344` n `228`; crypto_major avg `-1.6855` n `8`; equity avg `0.5013` n `69`; fx avg `-0.0172` n `6`; index avg `-0.2109` n `23`; metal avg `-0.504` n `18`; unknown avg `2.4973` n `422`
- 24h: commodity avg `0.9886` n `12`; crypto_alt avg `-0.0449` n `228`; crypto_major avg `-1.8626` n `8`; equity avg `0.1244` n `69`; fx avg `-0.0069` n `6`; index avg `0.2109` n `23`; metal avg `-0.1038` n `18`; unknown avg `4.6355` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2873`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
