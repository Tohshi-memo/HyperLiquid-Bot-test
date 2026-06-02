# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T23:52:19.851554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.47` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.0229` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7199` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5681` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.2303` n `12`; crypto_alt avg `0.4879` n `228`; crypto_major avg `0.4391` n `8`; equity avg `0.0402` n `69`; fx avg `0.0029` n `6`; index avg `0.15` n `23`; metal avg `0.2207` n `18`; unknown avg `1.0497` n `422`
- 1h: commodity avg `0.2286` n `12`; crypto_alt avg `0.0569` n `228`; crypto_major avg `0.6857` n `8`; equity avg `-0.2539` n `69`; fx avg `-0.0194` n `6`; index avg `0.0303` n `23`; metal avg `-0.2027` n `18`; unknown avg `0.1272` n `422`
- 4h: commodity avg `0.3638` n `12`; crypto_alt avg `-1.7801` n `228`; crypto_major avg `-1.6591` n `8`; equity avg `-0.091` n `69`; fx avg `-0.0601` n `6`; index avg `0.0608` n `23`; metal avg `-0.2668` n `18`; unknown avg `0.7095` n `422`
- 24h: commodity avg `0.5506` n `12`; crypto_alt avg `-5.3856` n `228`; crypto_major avg `-6.2758` n `8`; equity avg `0.8766` n `69`; fx avg `0.0481` n `6`; index avg `0.8369` n `23`; metal avg `0.0521` n `18`; unknown avg `0.1292` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
