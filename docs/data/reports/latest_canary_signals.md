# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T16:22:29.474245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.678` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.0055` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5509` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1569` n `12`; crypto_alt avg `0.3324` n `228`; crypto_major avg `0.0808` n `8`; equity avg `-0.0846` n `69`; fx avg `0.0271` n `6`; index avg `0.0675` n `23`; metal avg `-0.1605` n `18`; unknown avg `0.6523` n `422`
- 1h: commodity avg `0.0801` n `12`; crypto_alt avg `0.6488` n `228`; crypto_major avg `-0.1669` n `8`; equity avg `0.0525` n `69`; fx avg `0.0525` n `6`; index avg `0.1338` n `23`; metal avg `-0.0852` n `18`; unknown avg `0.6097` n `422`
- 4h: commodity avg `1.1043` n `12`; crypto_alt avg `-0.0283` n `228`; crypto_major avg `-1.5737` n `8`; equity avg `0.4318` n `69`; fx avg `-0.0097` n `6`; index avg `-0.0228` n `23`; metal avg `-0.4578` n `18`; unknown avg `0.9433` n `422`
- 24h: commodity avg `1.1841` n `12`; crypto_alt avg `0.261` n `228`; crypto_major avg `-1.9387` n `8`; equity avg `-0.124` n `69`; fx avg `0.0095` n `6`; index avg `0.207` n `23`; metal avg `-0.3109` n `18`; unknown avg `4.3584` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2894`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2151`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
