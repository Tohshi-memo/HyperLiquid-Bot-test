# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T18:22:17.641054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2123` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.258` n `12`; crypto_alt avg `0.776` n `228`; crypto_major avg `0.4991` n `8`; equity avg `0.1477` n `67`; fx avg `-0.0054` n `6`; index avg `0.0841` n `23`; metal avg `0.0433` n `18`; unknown avg `0.5903` n `396`
- 1h: commodity avg `-0.3001` n `12`; crypto_alt avg `0.8232` n `228`; crypto_major avg `0.7421` n `8`; equity avg `0.2724` n `67`; fx avg `-0.0017` n `6`; index avg `0.0635` n `23`; metal avg `0.0743` n `18`; unknown avg `1.7471` n `396`
- 4h: commodity avg `-0.5884` n `12`; crypto_alt avg `2.2329` n `228`; crypto_major avg `1.6239` n `8`; equity avg `0.6944` n `67`; fx avg `0.0078` n `6`; index avg `0.1412` n `23`; metal avg `0.2363` n `18`; unknown avg `2.1648` n `396`
- 24h: commodity avg `-0.0039` n `12`; crypto_alt avg `-1.6763` n `228`; crypto_major avg `-1.2587` n `8`; equity avg `-0.5849` n `67`; fx avg `0.0078` n `6`; index avg `-0.2196` n `23`; metal avg `-0.1742` n `18`; unknown avg `-0.8461` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
